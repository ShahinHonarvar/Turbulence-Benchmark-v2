def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(4, 9) if string[i].isalpha()]
    result = set()
    if len(letters) >= 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    substring = letters[i] + letters[j] + letters[k]
                    if substring == substring[::-1]:
                        result.add(substring)
                        for l in range(len(letters)):
                            if l != i and l != j and (l != k):
                                substring = letters[i] + letters[j] + letters[l] + letters[k]
                                if substring == substring[::-1]:
                                    result.add(substring)
                                    for m in range(len(letters)):
                                        if m != i and m != j and (m != k) and (m != l):
                                            substring = letters[i] + letters[j] + letters[l] + letters[m] + letters[k]
                                            if substring == substring[::-1]:
                                                result.add(substring)
    return result