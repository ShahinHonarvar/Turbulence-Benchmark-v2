def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 14):
        slice_ = s[i:i + 15]
        if slice_ == slice_[::-1]:
            palindromes.add(slice_)
    return palindromes