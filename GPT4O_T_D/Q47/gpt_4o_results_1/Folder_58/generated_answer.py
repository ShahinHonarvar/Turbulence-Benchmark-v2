def palindromes_of_specific_lengths(s: str) -> set:

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]
    s = s[125:284]
    results = set()
    for length in range(109, 127):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            letters_only = ''.join((ch.lower() for ch in sub if ch.isalpha()))
            if len(letters_only) == length and is_palindrome(letters_only):
                results.add(sub)
    return results