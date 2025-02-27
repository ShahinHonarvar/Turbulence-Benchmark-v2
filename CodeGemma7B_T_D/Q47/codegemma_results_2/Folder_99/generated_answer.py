def palindromes_of_specific_lengths(string):
    answer = set()
    for i in range(127, 289):
        for j in range(i + 119, i + 142):
            if j > len(string):
                continue
            palindrome = string[i:j]
            if palindrome == palindrome[::-1].lower():
                answer.add(palindrome)
    return answer