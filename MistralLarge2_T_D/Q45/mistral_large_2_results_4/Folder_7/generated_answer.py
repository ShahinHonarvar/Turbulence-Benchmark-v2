def palindromes_between_indices(s):
    letters = [c for c in s[1:10] if c.isalpha()]
    lower_letters = ''.join(letters).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_combinations(prefix, remaining, length):
        if length == 0:
            if is_palindrome(prefix):
                result.add(prefix)
        elif remaining:
            for i in range(len(remaining)):
                generate_combinations(prefix + remaining[i], remaining[:i] + remaining[i + 1:], length - 1)
    result = set()
    for length in range(7, len(lower_letters) + 1):
        generate_combinations('', lower_letters, length)
    return result