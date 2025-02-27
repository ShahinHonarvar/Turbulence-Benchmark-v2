def palindrome_of_length_at_least_n(st):
    answer = set()
    for i in range(len(st)):
        if st[i] >= 'a' and st[i] <= 'z':
            left = i
            right = i
            while left >= 0 and right < len(st) and (st[left] == st[right]):
                if right - left + 1 >= 19:
                    answer.add(st[left:right + 1])
                left -= 1
                right += 1
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(st) and (st[left] == st[right]):
                if right - left + 1 >= 19:
                    answer.add(st[left:right + 1])
                left -= 1
                right += 1
    return answer