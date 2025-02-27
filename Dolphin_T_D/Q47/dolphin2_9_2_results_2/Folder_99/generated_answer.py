def palindromes_of_specific_lengths(s):
    substring = s[127:289]
    palindromes = set()
    for length in range(119, 142):
        for i in range(len(substring) - length + 1):
            temp = substring[i:i + length]
            if temp == temp[::-1] and temp.isalpha():
                palindromes.add(temp)
    return palindromes