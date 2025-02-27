def palindromes_of_specific_lengths(s):
    substring = s[11:88].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 4, i + 6):
            if j < len(substring):
                temp = substring[i:j + 1]
                if temp == temp[::-1] and temp.isalpha():
                    palindromes.add(temp)
    return palindromes