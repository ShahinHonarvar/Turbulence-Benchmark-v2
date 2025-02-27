def palindrome_of_length_at_least_n(str):
    arr = []
    s = str.lower()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                temp = s[i:j + 1]
                if temp == temp[::-1] and len(temp) >= 68:
                    arr.append(temp)
    return set(arr)