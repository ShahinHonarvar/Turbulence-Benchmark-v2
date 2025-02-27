def palindromes_between_indices(str_arg):
    case_insensitive_str = str_arg.lower()
    all_palindromes = set()
    for i in range(2, 9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 9):
                for l in range(k + 1, 9):
                    for m in range(l + 1, 9):
                        substring = case_insensitive_str[i:j + 1]
                        if substring == substring[::-1] and len(substring) >= 4:
                            all_palindromes.add(substring)
    return all_palindromes