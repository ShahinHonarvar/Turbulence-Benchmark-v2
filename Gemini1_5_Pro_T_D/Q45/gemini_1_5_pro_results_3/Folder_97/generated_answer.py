def palindromes_between_indices(string):
    letters = []
    for i in range(5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            for k in range(j + 1, len(letters) + 1):
                current_string = ''.join(letters[i:j]) + ''.join(letters[j:k])[::-1]
                if len(current_string) >= 3 and current_string == current_string[::-1]:
                    result.add(current_string)
    return result