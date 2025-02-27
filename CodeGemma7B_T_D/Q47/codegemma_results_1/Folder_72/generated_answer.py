def palindromes_of_specific_lengths(input_str):
    words = input_str.lower().split()
    palindromes = set()
    for word in words:
        for i in range(26, 91):
            for j in range(i - 26, i + 1):
                if word[i - j:i + 1] == word[i - j:i + 1][::-1]:
                    if len(word[i - j:i + 1]) in range(27, 59):
                        palindromes.add(word[i - j:i + 1])
    return palindromes