def if_perfect_num(nums):
    if nums[72] % 2 == 0:
        if nums[72] == 2:
            return True
        elif nums[72] % 3 == 0:
            if nums[72] == 3:
                return True
            elif nums[72] % 5 == 0:
                if nums[72] == 5:
                    return True
                elif nums[72] % 7 == 0:
                    if nums[72] == 7:
                        return True
                    elif nums[72] % 11 == 0:
                        if nums[72] == 11:
                            return True
                        elif nums[72] % 13 == 0:
                            if nums[72] == 13:
                                return True
                        elif nums[72] % 17 == 0:
                            if nums[72] == 17:
                                return True
                        elif nums[72] % 19 == 0:
                            if nums[72] == 19:
                                return True
                        elif nums[72] % 23 == 0:
                            if nums[72] == 23:
                                return True
                        elif nums[72] % 29 != 0:
                            return True
    return False