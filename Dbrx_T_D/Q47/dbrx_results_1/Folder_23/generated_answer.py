def palindromes_of_specific_lengths(s):
    s = s.lower()
    length_range = range(17, 56)
    palindromes = {palindrome for i in length_range for palindrome in {s[j:k] for j in range(23, 94 - i + 1) for k in range(j + i, 94 - i + 1)} if palindrome == palindrome[::-1]}
    return palindromes