def palindromes_between_indices(s):
    letters = []
    for i in range(5, 8):
        letters.append(s[i].lower())
    palindromes = set()

    def generate_all_arrangements(arrangement, index):
        if index == len(arrangement):
            if len(arrangement) >= 4:
                palindrome = arrangement + arrangement[::-1]
                if ''.join(palindrome) == palindrome[::-1]:
                    palindromes.add(''.join(palindrome))
        else:
            generate_all_arrangements(arrangement + [arrangement[index]], index + 1)
            generate_all_arrangements(arrangement, index + 1)
    generate_all_arrangements([], 0)
    return palindromes