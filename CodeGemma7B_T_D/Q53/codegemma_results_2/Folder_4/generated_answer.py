def palindrome_of_length_at_least_n(str):
    str = str.lower()
    palindrome = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            if str[i] == str[j]:
                substring = str[i:j + 1]
                mid = len(substring) // 2
                left, right = (substring[:mid], substring[mid:])
                if left == right[::-1] and len(substring) >= 99:
                    palindrome.add(substring)
    return palindrome