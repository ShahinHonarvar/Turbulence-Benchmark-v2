def palindromes_of_specific_lengths(txt):

    def _is_palindrome(p):
        return p == p[::-1]

    def _convert_to_ascii(txt):
        return ''.join(filter(str.isalpha, txt))
    normalized_txt = _convert_to_ascii(txt.lower())
    start, end = (16, 60)
    palindromes = set()
    for i in range(start, end + 1):
        for j in range(i, end + 1):
            palindrome = normalized_txt[i:j]
            if _is_palindrome(palindrome) and 16 <= len(palindrome) <= 39:
                palindromes.add(palindrome)
    return palindromes