def palindromes_between_indices(string):
    if len(string) < 4 or string == string[::-1]:
        return set()
    answer = set()
    for i in range(4, len(string) - 3):
        for j in range(i + 1, len(string) - 2):
            for k in range(j + 1, len(string) - 1):
                palindrome = string[i:j + 1][::-1]
                if palindrome.lower() not in answer:
                    answer.add(palindrome.lower())
    return answer