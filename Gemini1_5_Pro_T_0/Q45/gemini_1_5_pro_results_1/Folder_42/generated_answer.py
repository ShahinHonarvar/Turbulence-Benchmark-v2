def palindromes_between_indices(string):
    letters = []
    for i in range(6, 10):
        if 0 <= i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    current = letters[i] + letters[j] + letters[k]
                    if current == current[::-1]:
                        result.add(current)
                    current = letters[i] + letters[k] + letters[j]
                    if current == current[::-1]:
                        result.add(current)
                    current = letters[j] + letters[i] + letters[k]
                    if current == current[::-1]:
                        result.add(current)
                    current = letters[j] + letters[k] + letters[i]
                    if current == current[::-1]:
                        result.add(current)
                    current = letters[k] + letters[i] + letters[j]
                    if current == current[::-1]:
                        result.add(current)
                    current = letters[k] + letters[j] + letters[i]
                    if current == current[::-1]:
                        result.add(current)
    return result