def palindrome_of_length_n(s):
    s = ''.join((ch for ch in s.lower() if ch.isalpha()))
    palindromes = set()
    len_s = len(s)
    for i in range(len_s - 463):
        sub = s[i:i + 464]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes