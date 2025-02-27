def palindromes_between_indices(string):
    letters = []
    for i in range(1, 5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for k in range(len(letters) - j + 1):
                permutation = letters[i:j]
                for l in range(k):
                    permutation.append(letters[j - l - 1])
                candidate = ''.join(permutation)
                if len(candidate) >= 5 and candidate == candidate[::-1]:
                    result.add(candidate)
    return result