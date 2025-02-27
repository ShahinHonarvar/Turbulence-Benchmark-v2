def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(32, 79 + 1):
        for j in range(i - 35, i + 1):
            if j >= 0 and j <= len(text) - 1 and (text[i] == text[j]):
                mid = (i + j) // 2
                if j - i + 1 == 35 and text[mid - 17:mid + 18] not in palindromes:
                    palindromes.add(text[mid - 17:mid + 18])
                elif j - i + 1 == 36 and text[mid - 18:mid + 19] not in palindromes:
                    palindromes.add(text[mid - 18:mid + 19])
                elif j - i + 1 == 37 and text[mid - 19:mid + 20] not in palindromes:
                    palindromes.add(text[mid - 19:mid + 20])
                elif j - i + 1 == 38 and text[mid - 20:mid + 21] not in palindromes:
                    palindromes.add(text[mid - 20:mid + 21])
                elif j - i + 1 == 39 and text[mid - 21:mid + 22] not in palindromes:
                    palindromes.add(text[mid - 21:mid + 22])
                elif j - i + 1 == 40 and text[mid - 22:mid + 23] not in palindromes:
                    palindromes.add(text[mid - 22:mid + 23])
                elif j - i + 1 == 41 and text[mid - 23:mid + 24] not in palindromes:
                    palindromes.add(text[mid - 23:mid + 24])
    return palindromes