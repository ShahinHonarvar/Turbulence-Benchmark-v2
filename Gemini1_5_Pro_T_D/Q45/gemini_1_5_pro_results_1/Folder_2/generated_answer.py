def palindromes_between_indices(string):
    letters = []
    for i in range(1, 6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters) - 5):
        for j in range(i + 1, len(letters) - 4):
            for k in range(j + 1, len(letters) - 3):
                for l in range(k + 1, len(letters) - 2):
                    for m in range(l + 1, len(letters) - 1):
                        for n in range(m + 1, len(letters)):
                            for p in range(6):
                                for q in range(p + 1, 6):
                                    palindrome = ''
                                    if p == 0:
                                        palindrome += letters[i]
                                    if p == 1:
                                        palindrome += letters[j]
                                    if p == 2:
                                        palindrome += letters[k]
                                    if p == 3:
                                        palindrome += letters[l]
                                    if p == 4:
                                        palindrome += letters[m]
                                    if p == 5:
                                        palindrome += letters[n]
                                    if q == 1:
                                        palindrome += letters[j]
                                    if q == 2:
                                        palindrome += letters[k]
                                    if q == 3:
                                        palindrome += letters[l]
                                    if q == 4:
                                        palindrome += letters[m]
                                    if q == 5:
                                        palindrome += letters[n]
                                    palindrome += palindrome[q - 1::-1]
                                    if len(palindrome) >= 6:
                                        palindromes.add(palindrome)
    return palindromes