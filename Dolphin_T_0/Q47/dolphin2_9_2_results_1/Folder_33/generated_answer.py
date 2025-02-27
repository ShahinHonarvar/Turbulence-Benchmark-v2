def palindromes_of_specific_lengths(s):
    substring = s[130:296]
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(substring) - length + 1):
            slice_ = substring[i:i + length]
            if slice_ == slice_[::-1] and all((c.isalpha() for c in slice_)):
                palindromes.add(slice_)
    return palindromes