def palindromes_of_specific_lengths(text):
    """Palindrome-finding function that handles the specific requirements."""
    substring = text[31:80]
    palindromes = {''.join(p) for p in combinations(substring, r) if p[0] >= 'a' and p[0] <= 'z' and (''.join(p) == ''.join(p)[::-1]) and (35 <= len(p) <= 41)}
    return palindromes if palindromes else set()