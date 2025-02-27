def return_nth_smallest_ascii(string):
    ans = min(string[25:46 + 1], key=ord)
    for c in string[25:46 + 1]:
        if ord(c) == ord(ans):
            ans = min(ans, c)
    return ans