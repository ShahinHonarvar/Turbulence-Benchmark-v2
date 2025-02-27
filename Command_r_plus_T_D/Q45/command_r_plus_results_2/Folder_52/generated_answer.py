def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    chars_between_indices = [char for char in s[:8] if char.isalpha()]
    unique_chars = set(chars_between_indices)
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(chars, length):
        if length == 0:
            return ['']
        if length == 1:
            return list(chars)
        palindromes = []
        for char in chars:
            for sub_palindrome in generate_palindromes(chars, length - 2):
                palindromes.append(char + sub_palindrome + char)
        return palindromes
    for char in unique_chars:
        for length in range(6, len(chars_between_indices) + 1):
            palindromes_to_add = [p for p in generate_palindromes([char], length) if is_palindrome(p)]
            palindromes.update(palindromes_to_add)
    return palindromes