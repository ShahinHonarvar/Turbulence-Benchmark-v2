def palindromes_between_indices(string):
    letters = []
    for i in range(2, 5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 4:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    for l in range(k + 1, len(letters)):
                        for permutation in [f'{letters[i]}{letters[j]}{letters[k]}{letters[l]}', f'{letters[i]}{letters[j]}{letters[l]}{letters[k]}', f'{letters[i]}{letters[k]}{letters[j]}{letters[l]}', f'{letters[i]}{letters[k]}{letters[l]}{letters[j]}', f'{letters[i]}{letters[l]}{letters[j]}{letters[k]}', f'{letters[i]}{letters[l]}{letters[k]}{letters[j]}', f'{letters[j]}{letters[i]}{letters[k]}{letters[l]}', f'{letters[j]}{letters[i]}{letters[l]}{letters[k]}', f'{letters[j]}{letters[k]}{letters[i]}{letters[l]}', f'{letters[j]}{letters[k]}{letters[l]}{letters[i]}', f'{letters[j]}{letters[l]}{letters[i]}{letters[k]}', f'{letters[j]}{letters[l]}{letters[k]}{letters[i]}', f'{letters[k]}{letters[i]}{letters[j]}{letters[l]}', f'{letters[k]}{letters[i]}{letters[l]}{letters[j]}', f'{letters[k]}{letters[j]}{letters[i]}{letters[l]}', f'{letters[k]}{letters[j]}{letters[l]}{letters[i]}', f'{letters[k]}{letters[l]}{letters[i]}{letters[j]}', f'{letters[k]}{letters[l]}{letters[j]}{letters[i]}', f'{letters[l]}{letters[i]}{letters[j]}{letters[k]}', f'{letters[l]}{letters[i]}{letters[k]}{letters[j]}', f'{letters[l]}{letters[j]}{letters[i]}{letters[k]}', f'{letters[l]}{letters[j]}{letters[k]}{letters[i]}', f'{letters[l]}{letters[k]}{letters[i]}{letters[j]}', f'{letters[l]}{letters[k]}{letters[j]}{letters[i]}']:
                            if permutation == permutation[::-1]:
                                result.add(permutation)
    return result