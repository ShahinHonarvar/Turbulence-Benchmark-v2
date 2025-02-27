def palindromes_of_specific_lengths(S):
    sub_string = S[16:73]
    palindromes = set()
    for i in range(50, 52):
        for j in range(len(sub_string) - i + 1):
            temp = sub_string[j:j + i]
            if temp.lower() == temp[::-1].lower():
                palindromes.add(temp)
    return palindromes