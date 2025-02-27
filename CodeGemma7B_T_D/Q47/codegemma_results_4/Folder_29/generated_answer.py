def palindromes_of_specific_lengths(txt):
    filtered_txt = txt[14:95].lower()
    palindromes = set()
    for i in range(len(filtered_txt) - 17):
        substring = filtered_txt[i:i + 18]
        if substring == substring[::-1]:
            palindromes.add(substring)
        for j in range(1, 56):
            if substring[-j:] == substring[:-j][::-1]:
                palindromes.add(substring)
    return palindromes