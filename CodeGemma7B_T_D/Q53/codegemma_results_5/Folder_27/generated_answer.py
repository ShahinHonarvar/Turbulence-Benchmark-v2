def palindrome_of_length_at_least_n(string):
    str1 = ''.join((char.lower() for char in string if char.isalpha()))
    lst = [word for word in str1.split() if len(word) >= 10]
    dp = {}
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i >= j:
                continue
            dp[lst[i] + lst[j]] = True
    res = set()
    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if i + j >= len(lst):
                continue
            x = 0
            y = j
            temp = ''
            while x < len(lst[i]) and y < len(lst[j]):
                if lst[i][x] == lst[j][y]:
                    temp += lst[i][x]
                    x += 1
                    y += 1
                else:
                    break
            if temp in dp.keys():
                res.add(temp)
    return res