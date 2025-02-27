def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    target_substring = ''.join([c for c in s[125:284] if c.isalpha()])
    for length in range(109, 127):
        for start in range(len(target_substring) - length + 1):
            current_substring = target_substring[start:start + length]
            if is_palindrome(current_substring):
                result.add(current_substring)
    return result