def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 463):
        candidate = s[i:i + 464]
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    for palindrome in palindromes:
        if not palindrome.isalpha():
            palindromes.remove(palindrome)
    return palindromes