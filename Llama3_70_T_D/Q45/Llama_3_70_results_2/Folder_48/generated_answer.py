def palindromes_between_indices(input_string):
    sub_string = ''.join(filter(str.isalpha, input_string[6:9])).lower()
    palindromes_set = set()

    def backtrack(first_half, remaining, length):
        if len(first_half) == length // 2:
            if length % 2 == 1:
                palindrome = first_half + remaining[0] + first_half[::-1]
                palindromes_set.add(palindrome)
                palindrome = first_half + first_half[::-1]
                palindromes_set.add(palindrome)
            else:
                palindrome = first_half + first_half[::-1]
                palindromes_set.add(palindrome)
            return
        for i in range(len(remaining)):
            if remaining[i] in first_half and remaining.count(remaining[i]) > 1:
                backtrack(first_half + remaining[i], remaining[:i] + remaining[i + 1:], length)
            elif remaining[i] not in first_half:
                backtrack(first_half + remaining[i], remaining[:i] + remaining[i + 1:], length)
    for length in range(4, len(sub_string) + 1):
        backtrack('', sub_string, length)
    return palindromes_set