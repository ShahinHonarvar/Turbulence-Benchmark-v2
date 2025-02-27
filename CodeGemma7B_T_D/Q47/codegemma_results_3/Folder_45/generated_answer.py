def palindromes_of_specific_lengths(text):
    begin, end = (70, 140)
    low, up = (ord('a'), ord('z'))
    ans = set()
    for i in range(begin, end + 1):
        if not low <= text[i] <= up:
            continue
        for j in range(min(i + 3, end - 60), i):
            if text[j:i + 1] == text[j:i + 1][::-1]:
                ans.add(text[j:i + 1])
    return ans