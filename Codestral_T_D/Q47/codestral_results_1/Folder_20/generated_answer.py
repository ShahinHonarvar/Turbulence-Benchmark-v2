def palindromes_of_specific_lengths(s):
    s = s[20:75].lower()
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(s) - length + 1):
            temp = s[i:i + length]
            if temp == temp[::-1] and temp.isalpha():
                palindromes.add(temp)
    return palindromes