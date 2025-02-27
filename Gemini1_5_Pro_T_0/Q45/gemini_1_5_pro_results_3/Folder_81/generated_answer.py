def palindromes_between_indices(string):
    letters = []
    for i in range(0, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            for k in range(len(substring) + 1):
                for l in range(k, len(substring) + 1):
                    candidate = substring[k:l]
                    if len(candidate) >= 3:
                        is_palindrome = True
                        for m in range(len(candidate) // 2):
                            if candidate[m] != candidate[len(candidate) - 1 - m]:
                                is_palindrome = False
                                break
                        if is_palindrome:
                            result.add(''.join(candidate))
    return result