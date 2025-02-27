def palindromes_of_specific_lengths(text):
    subtext = text[100:293]
    palindromes = set()
    for i in range(52):
        for j in range(i + 153, i + 183):
            if subtext[i] == subtext[j] and subtext[i + 1] == subtext[j - 1] and (subtext[i:j + 1] == subtext[s::-1]):
                str1 = ''.join((ch for ch in subtext[i:j + 1] if ch.isalpha()))
                if len(str1) == j - i + 1:
                    palindromes.add(str1)
    return palindromes