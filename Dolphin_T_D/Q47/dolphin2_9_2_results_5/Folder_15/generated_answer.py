def palindromes_of_specific_lengths(substring):
    substring = substring[:7]
    palindromes = set()
    for length in range(3, 7):
        for i in range(len(substring) - length + 1):
            temp = substring[i:i + length]
            if temp.lower() == temp[::-1].lower():
                if temp.isalpha():
                    palindromes.add(temp)
    return palindromes