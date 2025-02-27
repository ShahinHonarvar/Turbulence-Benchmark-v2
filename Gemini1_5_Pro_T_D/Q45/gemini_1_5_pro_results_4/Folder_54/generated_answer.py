def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(4, 10) if string[i].isalpha()]
    result = set()
    if len(letters) < 4:
        return result
    for i in range(len(letters) - 3):
        for j in range(i + 1, len(letters) - 2):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for p in [''.join(perm) for perm in [[letters[i], letters[j], letters[k], letters[l]], [letters[i], letters[j], letters[l], letters[k]], [letters[i], letters[k], letters[j], letters[l]], [letters[i], letters[k], letters[l], letters[j]], [letters[i], letters[l], letters[j], letters[k]], [letters[i], letters[l], letters[k], letters[j]], [letters[j], letters[i], letters[k], letters[l]], [letters[j], letters[i], letters[l], letters[k]], [letters[j], letters[k], letters[i], letters[l]], [letters[j], letters[k], letters[l], letters[i]], [letters[j], letters[l], letters[i], letters[k]], [letters[j], letters[l], letters[k], letters[i]], [letters[k], letters[i], letters[j], letters[l]], [letters[k], letters[i], letters[l], letters[j]], [letters[k], letters[j], letters[i], letters[l]], [letters[k], letters[j], letters[l], letters[i]], [letters[k], letters[l], letters[i], letters[j]], [letters[k], letters[l], letters[j], letters[i]], [letters[l], letters[i], letters[j], letters[k]], [letters[l], letters[i], letters[k], letters[j]], [letters[l], letters[j], letters[i], letters[k]], [letters[l], letters[j], letters[k], letters[i]], [letters[l], letters[k], letters[i], letters[j]], [letters[l], letters[k], letters[j], letters[i]]]]:
                        if p == p[::-1]:
                            result.add(p)
    return result