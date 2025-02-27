def palindromes_between_indices(string):
    letters = []
    for i in range(3, 7):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                current_string = letters[i] + letters[j] + letters[k]
                if current_string == current_string[::-1]:
                    result.add(current_string)
                current_string = letters[i] + letters[k] + letters[j]
                if current_string == current_string[::-1]:
                    result.add(current_string)
                current_string = letters[j] + letters[i] + letters[k]
                if current_string == current_string[::-1]:
                    result.add(current_string)
                current_string = letters[j] + letters[k] + letters[i]
                if current_string == current_string[::-1]:
                    result.add(current_string)
                current_string = letters[k] + letters[i] + letters[j]
                if current_string == current_string[::-1]:
                    result.add(current_string)
                current_string = letters[k] + letters[j] + letters[i]
                if current_string == current_string[::-1]:
                    result.add(current_string)
    return result