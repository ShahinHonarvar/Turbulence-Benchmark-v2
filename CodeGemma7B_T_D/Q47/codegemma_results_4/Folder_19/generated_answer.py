def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 55):
        for j in range(3, 8):
            if s[i:i + j] == s[i:i + j][::-1]:
                if s[i:i + j].lower() not in palindromes:
                    palindromes.add(s[i:i + j].lower())
    return palindromes