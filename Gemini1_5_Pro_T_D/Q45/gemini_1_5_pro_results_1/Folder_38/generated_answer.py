def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(3, 9) if string[i].lower() in 'abcdefghijklmnopqrstuvwxyz']
    result = set()
    if len(letters) < 5:
        return result
    for i in range(len(letters) - 4):
        for j in range(i + 4, len(letters)):
            current = letters[i:j + 1]
            if current == current[::-1]:
                result.add(''.join(current))
    return result