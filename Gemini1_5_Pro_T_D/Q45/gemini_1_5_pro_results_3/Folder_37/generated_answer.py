def palindromes_between_indices(string):
    letters = []
    for i in range(1, 5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for k in range(len(letters) + 1):
                permutation = letters[i:j]
                for l in range(len(permutation) // 2):
                    permutation[l], permutation[len(permutation) - l - 1] = (permutation[len(permutation) - l - 1], permutation[l])
                candidate = letters[:i] + permutation + letters[j:]
                if len(candidate) >= 5 and candidate == candidate[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes