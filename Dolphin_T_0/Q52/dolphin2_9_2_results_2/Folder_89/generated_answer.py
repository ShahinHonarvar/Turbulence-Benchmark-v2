def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 36):
        String = s[i:i + 37]
        if String == String[::-1]:
            palindromes.add(String)
    return palindromes