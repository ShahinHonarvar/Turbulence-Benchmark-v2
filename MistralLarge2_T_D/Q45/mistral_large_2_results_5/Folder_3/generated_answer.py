def palindromes_between_indices(s):
    letters = [c for c in s[7:10] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(prefix, suffix, remaining_letters):
        if len(prefix) >= 3 and is_palindrome(prefix):
            palindromes.add(prefix)
        if remaining_letters:
            for i in range(len(remaining_letters)):
                new_prefix = prefix + remaining_letters[i]
                new_suffix = remaining_letters[i] + suffix
                new_remaining = remaining_letters[:i] + remaining_letters[i + 1:]
                generate_palindromes(new_prefix, new_suffix, new_remaining)
    generate_palindromes('', '', letters)
    return palindromes