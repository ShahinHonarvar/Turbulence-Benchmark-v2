def palindrome_of_length_n(s):
    palindromes = set()
    if len(s) < 49:
        return palindromes
    for i in range(len(s) - 48):
        candidate = s[i:i + 49].lower()
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes