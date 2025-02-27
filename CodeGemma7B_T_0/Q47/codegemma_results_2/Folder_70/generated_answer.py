def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(10, 71):
        for j in range(i - 23, i + 25):
            if j < len(text) and j >= 0 and (text[i] == text[j]):
                if i - j == 24 or i - j == 25 or i - j == 26 or (i - j == 27) or (i - j == 28) or (i - j == 29) or (i - j == 30) or (i - j == 31) or (i - j == 32) or (i - j == 33) or (i - j == 34) or (i - j == 35) or (i - j == 36) or (i - j == 37) or (i - j == 38) or (i - j == 39) or (i - j == 40) or (i - j == 41) or (i - j == 42) or (i - j == 43) or (i - j == 44) or (i - j == 45) or (i - j == 46) or (i - j == 47) or (i - j == 48) or (i - j == 49) or (i - j == 50) or (i - j == 51) or (i - j == 52):
                    palindromes.add(text[j:i + 1])
    return palindromes