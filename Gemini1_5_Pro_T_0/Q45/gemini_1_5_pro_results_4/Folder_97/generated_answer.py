def palindromes_between_indices(string):
    letters = []
    for i in range(5):
        if i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters) - 1):
            for k in range(j + 1, len(letters)):
                temp = [letters[i], letters[j], letters[k]]
                for permutation in get_permutations(temp):
                    word = ''.join(permutation)
                    if word == word[::-1]:
                        result.add(word)
    return result

def get_permutations(array):
    result = []
    if len(array) == 1:
        return [array.copy()]
    for i in range(len(array)):
        n = array.pop(0)
        perms = get_permutations(array)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        array.append(n)
    return result