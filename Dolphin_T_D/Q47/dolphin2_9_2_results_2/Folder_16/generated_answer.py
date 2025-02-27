def palindromes_of_specific_lengths(word):
    sub_str = word[15:87]
    palindromes = set()
    for size in range(51, 61):
        sub_substr = sub_str[size * -1:]
        for i in range(len(sub_substr) - size + 1):
            temp = sub_substr[i:i + size]
            if temp.lower() == temp[::-1].lower():
                palindromes.add(temp)
    return palindromes