def palindromes_between_indices(string):
    result = []
    for i in range(2, 5):
        for j in range(len(string) - i):
            if string[j:j + i].lower() == string[j:j + i][::-1].lower():
                result.append(string[j:j + i].lower())
    return set(result)