def palindrome_of_length_at_least_n(s: str) -> set:
    english_letters_only = set(s.lower()) & set('abcdefghijklmnopqrstuvwxyz')
    palindromes = {palindrome for length in range(91, len(s) + 1) for palindrome in find_palindromes(s, length, english_letters_only)}
    return palindromes

def find_palindromes(s: str, length: int, valid_chars: set) -> set:
    palindromes = set()
    for start in range(len(s) - length + 1):
        candidate = s[start:start + length]
        if set(candidate) <= valid_chars and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes