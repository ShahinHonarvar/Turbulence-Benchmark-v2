def all_left_right_truncatable_prime(nums):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    answer = []
    for i in prime:
        if i >= nums[92]:
            continue
        i_str = str(i)
        flag = True
        for j in range(1, len(i_str)):
            left, right = (int(i_str[0:j]), int(i_str[j:]))
            if left == 0 or right == 0 or left == 1 or (right == 1) or (left not in prime) or (right not in prime):
                flag = False
                break
        if flag:
            answer.append(i)
    return sorted(answer) or []