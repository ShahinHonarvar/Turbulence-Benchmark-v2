def palindromes_between_indices(string):
    letters = []
    for i in range(3, 10):
        if 9 < len(string) and 'a' <= string[i].lower() <= 'z':
            letters.append(string[i].lower())
        elif i < len(string):
            continue
        else:
            break
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                substring = letters[i] + letters[j] + letters[k]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    substring = letters[i] + letters[j] + letters[k] + letters[l]
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        substring = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if substring == substring[::-1]:
                            palindromes.add(substring)
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        for n in range(m + 1, len(letters)):
                            substring = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]
                            if substring == substring[::-1]:
                                palindromes.add(substring)
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        for n in range(m + 1, len(letters)):
                            for o in range(n + 1, len(letters)):
                                substring = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n] + letters[o]
                                if substring == substring[::-1]:
                                    palindromes.add(substring)
    return palindromes