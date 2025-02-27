from collections import defaultdict

def palindrome_of_length_255(s):
    forward_chars, backward_chars = (defaultdict(set), defaultdict(set))
    for idx, char in enumerate(s):
        forward_chars[idx].add(char)
        backward_chars[len(s) - idx].add(char)

    def generate_palindrome(forward_idx, backward_idx):
        if forward_idx > backward_idx:
            return {''.join(elem) for elem in forward_chars[forward_idx]}
        if s[forward_idx] != s[backward_idx]:
            return set()
        return {char + palindrome + rev_char for char in forward_chars[forward_idx] for rev_char in backward_chars[backward_idx] for palindrome in generate_palindrome(forward_idx + 1, backward_idx - 1)}
    return generate_palindrome(0, len(s) - 1)